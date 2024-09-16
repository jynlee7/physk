// shm_3d.js

var scene = new THREE.Scene();
var camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
var renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

// Create the mass (block)
var massGeometry = new THREE.BoxGeometry(1, 1, 1);
var massMaterial = new THREE.MeshBasicMaterial({color: 0xff0000});
var mass = new THREE.Mesh(massGeometry, massMaterial);
scene.add(mass);

camera.position.z = 10;

// SHM variables
var k = 1;  // Spring constant
var m = 1;  // Mass
var x = 5;  // Initial displacement
var v = 0;  // Initial velocity
var a = 0;  // Initial acceleration

function animate() {
    requestAnimationFrame(animate);

    // Update acceleration based on Hooke's Law
    a = (-k / m) * x;

    // Update velocity and position
    v += a * 0.01;
    x += v * 0.01;

    // Update mass position
    mass.position.x = x;

    renderer.render(scene, camera);
}

animate();
