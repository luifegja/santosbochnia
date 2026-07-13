# -*- coding: utf-8 -*-
"""Renderiza criativos HTML em PNG 1080x1350 via Edge headless (CDP).

Uso:  python render.py <arquivo.html> <pasta-destino> <prefixo>
Ex.:  python render.py previdenciario-carrossel-01.html ../previdenciario carrossel-01

Cada elemento .card vira <prefixo>-card-N.png (na ordem do DOM).
Um elemento .card--static vira estatico-NN.png (NN do sufixo do prefixo).
Requer: servidor http na raiz do projeto (o script sobe um em 8742) e websocket-client.
"""
import base64, json, os, subprocess, sys, time, urllib.request
import websocket

EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
PORT_CDP = 9444
PORT_HTTP = 8742
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def cdp(ws, _id, method, params=None):
    ws.send(json.dumps({"id": _id, "method": method, "params": params or {}}))
    while True:
        msg = json.loads(ws.recv())
        if msg.get("id") == _id:
            return msg.get("result", {})

def main(html_file, dest, prefix):
    html_abs = os.path.abspath(html_file)
    rel = os.path.relpath(html_abs, ROOT).replace("\\", "/")
    url = f"http://localhost:{PORT_HTTP}/{urllib.request.quote(rel)}"

    server = subprocess.Popen([sys.executable, "-m", "http.server", str(PORT_HTTP)],
                              cwd=ROOT, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    edge = subprocess.Popen([EDGE, "--headless=new", "--disable-gpu",
                             f"--remote-debugging-port={PORT_CDP}", "--remote-allow-origins=*",
                             "--hide-scrollbars", "about:blank"],
                            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(4)
    try:
        req = urllib.request.Request(f"http://localhost:{PORT_CDP}/json/new?about:blank", method="PUT")
        with urllib.request.urlopen(req) as r:
            target = json.load(r)
        ws = websocket.create_connection(target["webSocketDebuggerUrl"], timeout=120)
        i = [0]
        def call(method, params=None):
            i[0] += 1
            return cdp(ws, i[0], method, params)

        call("Emulation.setDeviceMetricsOverride", {"width": 1400, "height": 1500, "deviceScaleFactor": 1, "mobile": False})
        call("Page.enable")
        call("Page.navigate", {"url": url})
        time.sleep(3)
        # espera fontes e imagens
        call("Runtime.evaluate", {"expression": "document.fonts.ready.then(()=>1)", "awaitPromise": True})
        call("Runtime.evaluate", {"expression": """
          Promise.all([...document.images].map(im => im.complete ? 1 :
            new Promise(r => { im.onload = im.onerror = r; }))).then(()=>1)""", "awaitPromise": True})
        time.sleep(1)

        boxes = json.loads(call("Runtime.evaluate", {"expression": """
          JSON.stringify([...document.querySelectorAll('.card')].map(c => {
            const r = c.getBoundingClientRect();
            return {x: r.x + scrollX, y: r.y + scrollY, w: r.width, h: r.height,
                    static: c.classList.contains('card--static')};
          }))""", "returnByValue": True})["result"]["value"])

        os.makedirs(dest, exist_ok=True)
        n_carousel = 0
        num = prefix.split("-")[-1] if prefix.split("-")[-1].isdigit() else "01"
        for b in boxes:
            if b["static"]:
                out = os.path.join(dest, f"estatico-{num}.png")
            else:
                n_carousel += 1
                out = os.path.join(dest, f"{prefix}-card-{n_carousel}.png")
            res = call("Page.captureScreenshot", {"format": "png", "captureBeyondViewport": True,
                "clip": {"x": b["x"], "y": b["y"], "width": b["w"], "height": b["h"], "scale": 1}})
            with open(out, "wb") as f:
                f.write(base64.b64decode(res["data"]))
            print("OK", out, f'{b["w"]:.0f}x{b["h"]:.0f}')
        ws.close()
    finally:
        edge.terminate()
        server.terminate()

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])
