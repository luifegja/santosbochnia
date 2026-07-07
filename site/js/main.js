/* Santos & Bochnia — main.js
   Comportamento compartilhado: header, reveals, contadores, FAQ.
   Toda animação respeita prefers-reduced-motion; a conversão (links wa.me)
   nunca depende deste arquivo. */
(function () {
  "use strict";

  document.documentElement.classList.remove("no-js");

  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (reduceMotion) document.documentElement.classList.add("no-motion");

  /* ---------- Header: estado ao rolar ---------- */
  var header = document.querySelector(".site-header");
  if (header) {
    var onScroll = function () {
      header.classList.toggle("is-scrolled", window.scrollY > 24);
    };
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
  }

  /* ---------- Reveals ---------- */
  var revealEls = Array.prototype.slice.call(document.querySelectorAll(".rv"));
  if (reduceMotion || !("IntersectionObserver" in window)) {
    revealEls.forEach(function (el) { el.classList.add("is-in"); });
  } else if (revealEls.length) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        var el = entry.target;
        var delay = parseFloat(el.getAttribute("data-rv-delay") || "0");
        el.style.transitionDelay = delay ? delay + "s" : "";
        el.classList.add("is-in");
        io.unobserve(el);
      });
    }, { threshold: 0.12, rootMargin: "0px 0px -8% 0px" });
    revealEls.forEach(function (el) { io.observe(el); });
  }

  /* ---------- Contadores ---------- */
  var counters = Array.prototype.slice.call(document.querySelectorAll("[data-count]"));
  function renderFinal(el) {
    el.textContent = el.getAttribute("data-count");
  }
  if (reduceMotion || !("IntersectionObserver" in window)) {
    counters.forEach(renderFinal);
  } else if (counters.length) {
    var cio = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        var el = entry.target;
        cio.unobserve(el);
        var target = parseInt(el.getAttribute("data-count"), 10);
        if (isNaN(target)) return renderFinal(el);
        var dur = 1400;
        var t0 = null;
        function tick(t) {
          if (!t0) t0 = t;
          var p = Math.min((t - t0) / dur, 1);
          var eased = 1 - Math.pow(1 - p, 3);
          el.textContent = String(Math.round(target * eased));
          if (p < 1) requestAnimationFrame(tick);
        }
        requestAnimationFrame(tick);
      });
    }, { threshold: 0.6 });
    counters.forEach(function (el) { cio.observe(el); });
  }

  /* ---------- FAQ: fecha os irmãos ao abrir ---------- */
  document.querySelectorAll(".faq").forEach(function (group) {
    group.addEventListener("toggle", function (e) {
      var d = e.target;
      if (d.tagName === "DETAILS" && d.open) {
        group.querySelectorAll("details[open]").forEach(function (other) {
          if (other !== d) other.open = false;
        });
      }
    }, true);
  });

  /* ---------- GSAP (opcional): parallax leve em imagens marcadas ---------- */
  if (!reduceMotion && window.gsap && window.ScrollTrigger) {
    gsap.registerPlugin(ScrollTrigger);
    gsap.utils.toArray("[data-parallax]").forEach(function (el) {
      gsap.to(el, {
        yPercent: parseFloat(el.getAttribute("data-parallax")) || -8,
        ease: "none",
        scrollTrigger: { trigger: el.parentElement, start: "top bottom", end: "bottom top", scrub: 0.6 }
      });
    });
  }
})();
