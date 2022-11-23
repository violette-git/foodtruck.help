let tl = gsap.timeline({repeat:-1})

// add the tweens to the timeline - Note we're using tl.to not gsap.to
tl.to(".neonText", { duration: "random(0,1)", display:"none",opacity:0,yoyo: true, });
tl.to(".neonText", { duration: "random(0,1)", display:"block",opacity:100,yoyo: true, });
tl.to(".neonText", { duration: "random(0,1)", display:"none",opacity:0,yoyo: true, });
tl.to(".neonText", { duration: "random(0,1)", display:"block",opacity:100,yoyo: true, });
tl.to(".neonText", { duration: "random(0,1)", display:"none",opacity:0,yoyo: true, });
tl.to(".neonText", { duration: "random(0,1)", display:"block",opacity:100,yoyo: true, });
tl.to(".neonText", { duration: "random(0,1)", display:"none",opacity:0,yoyo: true, });
tl.to(".neonText", { duration: "random(0,1)", display:"block",opacity:100,yoyo: true, });
tl.to(".neonText", { duration: "random(0,1)", display:"none",opacity:0,yoyo: true, });
tl.to(".neonText", { duration: "random(0,1)", display:"block",opacity:100,yoyo: true, });
tl.to(".neonText", { duration: "random(0,1)", display:"none",opacity:0,yoyo: true, });
tl.to(".neonText", { duration: "random(0,1)", display:"block",opacity:100,yoyo: true, });
tl.to(".neonText", { duration: "random(0,1)", display:"none",opacity:0,yoyo: true, });
tl.to(".neonText", { duration: "random(0,1)", display:"block",opacity:100,yoyo: true, });
tl.to(".neonText", { duration: "random(0,1)", display:"none",opacity:0,yoyo: true, });
tl.to(".neonText", { duration: "random(0,1)", display:"block",opacity:100,yoyo: true, });
tl.to(".neonText", { duration: "random(0,1)", display:"none",opacity:0,yoyo: true, });
tl.to(".neonText", { duration: "random(0,1)", display:"block",opacity:100,yoyo: true, });
tl.to(".neonText", { duration: "random(0,1)", display:"none",opacity:0,yoyo: true, });
tl.to(".neonText", { duration: "random(0,1)", display:"block",opacity:100,yoyo: true, });
tl.to(".neonText", { duration: "random(0,1)", display:"none",opacity:0,yoyo: true, });
tl.to(".neonText", { duration: "random(0,1)", display:"block",opacity:100,yoyo: true, });
tl.to(".neonText", { duration: "random(0,1)", display:"none",opacity:0,yoyo: true, });
tl.to(".neonText", { duration: "random(0,1)", display:"block",opacity:100,yoyo: true, });
tl.to(".neonText", { duration: "random(0,1)", display:"none",opacity:0,yoyo: true, });
tl.to(".neonText", { duration: "random(0,1)", display:"block",opacity:100,yoyo: true, });
tl.to(".neonText", { duration: "random(0,1)", display:"none",opacity:0,yoyo: true, });
tl.to(".neonText", { duration: "random(0,1)", display:"block",opacity:100,yoyo: true, });
tl.to(".neonText", { duration: "random(0,1)", display:"none",opacity:0,yoyo: true, });
tl.to(".neonText", { duration: "random(0,1)", display:"block",opacity:100,yoyo: true, });
tl.to(".neonText", { duration: "random(0,1)", display:"none",opacity:0,yoyo: true, });
tl.to(".neonText", { duration: "random(0,1)", display:"block",opacity:100,yoyo: true, });
tl.to(".neonText", { duration: "random(0,1)", display:"none",opacity:0,yoyo: true, });
tl.to(".neonText", { duration: "random(0,1)", display:"block",opacity:100,yoyo: true, });
tl.to(".neonText", { duration: "random(0,1)", display:"none",opacity:0,yoyo: true, });
tl.to(".neonText", { duration: "random(0,1)", display:"block",opacity:100,yoyo: true, });
tl.to(".neonText", { duration: "random(0,1)", display:"none",opacity:0,yoyo: true, });
tl.to(".neonText", { duration: "random(0,1)", display:"block",opacity:100,yoyo: true, });
tl.to(".neonText", { duration: "random(0,1)", display:"none",opacity:0,yoyo: true, });
tl.to(".neonText", { duration: "random(0,1)", display:"block",opacity:100,yoyo: true, });
tl.to(".neonText", { duration: "random(0,1)", display:"none",opacity:0,yoyo: true, });
tl.to(".neonText", { duration: "random(0,1)", display:"block",opacity:100,yoyo: true, });
tl.to(".neonText", { duration: "random(0,1)", display:"none",opacity:0,yoyo: true, });
tl.to(".neonText", { duration: "random(0,1)", display:"block",opacity:100,yoyo: true, });



let button = document.getElementById("get-started");
console.log(button)

// button.addEventListener('mouseenter', () => {
//     gsap.to(button, {
//         scale:1.2
//     })    
// })    
var animation = gsap.timeline({ paused: true });
  animation.to(button, {scale: 1.05, duration: .5, ease: "power1.inOut"});
  button.addEventListener("mouseenter", function () {animation.play();});
  button.addEventListener("mouseleave", function () {animation.reverse();});  
