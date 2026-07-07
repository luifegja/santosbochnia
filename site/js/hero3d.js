/* Santos & Bochnia — hero3d.js
   Cena "Maré de precisão": malha de ondas navy + partículas turquesa +
   monograma SB extrudado (vidro-metálico), com degradação graciosa.
   Carrega Three.js dinamicamente APÓS window.load — o LCP nunca espera o 3D.
   Fallback estático: classe .is-static no container (monograma em marca-d'água). */

(function () {
  "use strict";

  var host = document.getElementById("hero-3d");
  if (!host) return;

  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var isMobile = window.matchMedia("(max-width: 768px)").matches;
  var lowEnd = (navigator.deviceMemory && navigator.deviceMemory <= 4);

  function fallback() { host.classList.add("is-static"); }

  if (reduceMotion) return fallback();

  // sonda de WebGL antes de baixar ~600KB de Three.js
  try {
    var probe = document.createElement("canvas");
    var gl = probe.getContext("webgl2") || probe.getContext("webgl");
    if (!gl) return fallback();
  } catch (e) { return fallback(); }

  var start = function () {
    import("https://cdn.jsdelivr.net/npm/three@0.158.0/+esm").then(function (THREE) {
      try { init(THREE); } catch (e) { fallback(); }
    }).catch(fallback);
  };
  if (document.readyState === "complete") start();
  else window.addEventListener("load", start);

  /* ---------- simplex noise 2D compacto (Gustavson, adaptado) ---------- */
  function makeNoise() {
    var grad = [[1,1],[-1,1],[1,-1],[-1,-1],[1,0],[-1,0],[0,1],[0,-1]];
    var p = new Uint8Array(512), perm = new Uint8Array(512);
    var seed = 47;
    for (var i = 0; i < 256; i++) p[i] = i;
    for (i = 255; i > 0; i--) {
      seed = (seed * 16807) % 2147483647;
      var r = seed % (i + 1);
      var t = p[i]; p[i] = p[r]; p[r] = t;
    }
    for (i = 0; i < 512; i++) perm[i] = p[i & 255];
    var F2 = 0.5 * (Math.sqrt(3) - 1), G2 = (3 - Math.sqrt(3)) / 6;
    return function (xin, yin) {
      var s = (xin + yin) * F2, i0 = Math.floor(xin + s), j0 = Math.floor(yin + s);
      var tt = (i0 + j0) * G2, x0 = xin - (i0 - tt), y0 = yin - (j0 - tt);
      var i1 = x0 > y0 ? 1 : 0, j1 = x0 > y0 ? 0 : 1;
      var x1 = x0 - i1 + G2, y1 = y0 - j1 + G2, x2 = x0 - 1 + 2 * G2, y2 = y0 - 1 + 2 * G2;
      var ii = i0 & 255, jj = j0 & 255, n = 0, t0, gi;
      t0 = 0.5 - x0 * x0 - y0 * y0;
      if (t0 > 0) { gi = grad[perm[ii + perm[jj]] % 8]; t0 *= t0; n += t0 * t0 * (gi[0] * x0 + gi[1] * y0); }
      t0 = 0.5 - x1 * x1 - y1 * y1;
      if (t0 > 0) { gi = grad[perm[ii + i1 + perm[jj + j1]] % 8]; t0 *= t0; n += t0 * t0 * (gi[0] * x1 + gi[1] * y1); }
      t0 = 0.5 - x2 * x2 - y2 * y2;
      if (t0 > 0) { gi = grad[perm[ii + 1 + perm[jj + 1]] % 8]; t0 *= t0; n += t0 * t0 * (gi[0] * x2 + gi[1] * y2); }
      return 70 * n;
    };
  }

  function init(THREE) {
    var W = host.clientWidth, H = host.clientHeight;
    var renderer = new THREE.WebGLRenderer({ alpha: true, antialias: !isMobile, powerPreference: "low-power" });
    renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, isMobile || lowEnd ? 1.5 : 2));
    renderer.setSize(W, H);
    host.appendChild(renderer.domElement);

    var scene = new THREE.Scene();
    var camera = new THREE.PerspectiveCamera(42, W / H, 0.1, 200);
    camera.position.set(0, 4.2, 30);

    var noise = makeNoise();

    /* ----- malha de ondas ----- */
    var segX = isMobile || lowEnd ? 60 : 110;
    var segY = isMobile || lowEnd ? 30 : 55;
    var planeGeo = new THREE.PlaneGeometry(120, 60, segX, segY);
    planeGeo.rotateX(-Math.PI / 2.35);
    var basePos = planeGeo.attributes.position.array.slice();

    // campo de pontos discreto (sem wireframe — o grid ficava pesado demais)
    var pts = new THREE.Points(planeGeo, new THREE.PointsMaterial({
      color: 0x77b9c9, size: isMobile ? 0.13 : 0.11, transparent: true, opacity: 0.32, sizeAttenuation: true
    }));
    pts.position.set(0, -9, -9);
    scene.add(pts);

    /* ----- partículas em deriva ----- */
    var N = isMobile || lowEnd ? 90 : 170;
    var pGeo = new THREE.BufferGeometry();
    var pArr = new Float32Array(N * 3), pSpeed = new Float32Array(N);
    for (var i = 0; i < N; i++) {
      pArr[i * 3] = (Math.random() - 0.5) * 70;
      pArr[i * 3 + 1] = Math.random() * 26 - 6;
      pArr[i * 3 + 2] = (Math.random() - 0.5) * 30 - 4;
      pSpeed[i] = 0.004 + Math.random() * 0.01;
    }
    pGeo.setAttribute("position", new THREE.BufferAttribute(pArr, 3));
    var drift = new THREE.Points(pGeo, new THREE.PointsMaterial({
      color: 0x9ad7e9, size: 0.13, transparent: true, opacity: 0.22, sizeAttenuation: true
    }));
    scene.add(drift);

    /* ----- monograma SB extrudado (enhancement, desktop) ----- */
    var mono = null;
    if (!isMobile && !lowEnd) {
      Promise.all([
        import("https://cdn.jsdelivr.net/npm/three@0.158.0/examples/jsm/loaders/SVGLoader.js/+esm"),
        import("https://cdn.jsdelivr.net/npm/three@0.158.0/examples/jsm/environments/RoomEnvironment.js/+esm")
      ]).then(function (mods) {
        var SVGLoader = mods[0].SVGLoader;
        var RoomEnvironment = mods[1].RoomEnvironment;
        new SVGLoader().load("assets/img/monograma-sb.svg", function (data) {
          try {
            var shapes = [];
            data.paths.forEach(function (path) {
              SVGLoader.createShapes(path).forEach(function (s) { shapes.push(s); });
            });
            if (!shapes.length) return;
            var geo = new THREE.ExtrudeGeometry(shapes, {
              depth: 60, bevelEnabled: true, bevelThickness: 6, bevelSize: 4, bevelSegments: 3, curveSegments: 10
            });
            geo.center();
            var pmrem = new THREE.PMREMGenerator(renderer);
            scene.environment = pmrem.fromScene(new RoomEnvironment(), 0.04).texture;
            var mat = new THREE.MeshPhysicalMaterial({
              color: 0x9ad7e9, metalness: 0.55, roughness: 0.3,
              clearcoat: 0.6, clearcoatRoughness: 0.25,
              transparent: true, opacity: 0.9
            });
            mono = new THREE.Mesh(geo, mat);
            var s = 0.0105;
            mono.scale.set(s, -s, s); // SVG tem Y para baixo
            mono.position.set(10.6, 1.1, 5);
            mono.rotation.x = 0.06;
            scene.add(mono);
          } catch (e) { /* segue só com a malha */ }
        }, undefined, function () { /* sem monograma */ });
      }).catch(function () { /* sem monograma */ });
    }

    /* ----- interação e loop ----- */
    var mouseX = 0, mouseY = 0, targX = 0, targY = 0;
    if (!isMobile) {
      window.addEventListener("pointermove", function (e) {
        targX = (e.clientX / window.innerWidth - 0.5) * 2;
        targY = (e.clientY / window.innerHeight - 0.5) * 2;
      }, { passive: true });
    }

    var visible = true, pageVisible = true;
    new IntersectionObserver(function (entries) {
      visible = entries[0].isIntersecting;
    }, { threshold: 0.02 }).observe(host);
    document.addEventListener("visibilitychange", function () {
      pageVisible = document.visibilityState === "visible";
    });

    window.addEventListener("resize", function () {
      W = host.clientWidth; H = host.clientHeight;
      camera.aspect = W / H;
      camera.updateProjectionMatrix();
      renderer.setSize(W, H);
    });

    var clock = new THREE.Clock();
    var pos = planeGeo.attributes.position;

    function animate() {
      requestAnimationFrame(animate);
      if (!visible || !pageVisible) return;
      var t = clock.getElapsedTime();

      // ondas: desloca o eixo "para cima" da malha rotacionada (y global)
      for (var i = 0; i < pos.count; i++) {
        var ix = i * 3;
        var x = basePos[ix], z = basePos[ix + 2];
        var h = noise(x * 0.045 + t * 0.05, z * 0.06 + t * 0.038) * 1.7
              + noise(x * 0.012 - t * 0.02, z * 0.018) * 2.8;
        pos.array[ix + 1] = basePos[ix + 1] + h;
      }
      pos.needsUpdate = true;

      // partículas sobem lentamente e reciclam
      var pp = pGeo.attributes.position;
      for (var j = 0; j < N; j++) {
        pp.array[j * 3 + 1] += pSpeed[j];
        if (pp.array[j * 3 + 1] > 22) pp.array[j * 3 + 1] = -6;
      }
      pp.needsUpdate = true;

      // monograma: rotação 1 volta / ~40s + flutuação
      if (mono) {
        mono.rotation.y = t * (Math.PI * 2 / 40);
        mono.position.y = 1.1 + Math.sin(t * 0.5) * 0.35;
      }

      // parallax suave do mouse
      mouseX += (targX - mouseX) * 0.04;
      mouseY += (targY - mouseY) * 0.04;
      camera.position.x = mouseX * 1.6;
      camera.position.y = 4.2 - mouseY * 0.9;
      camera.lookAt(0, 1.5, 0);

      renderer.render(scene, camera);
    }
    animate();
  }
})();
