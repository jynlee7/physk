// pendulum_3d.js

var scene = new THREE.Scene();
var camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
var renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

// Create the pendulum arm
var armGeometry = new THREE.CylinderGeometry(0.1, 0.1, 5, 32);
var armMaterial = new THREE.MeshBasicMaterial({color: 0x0000ff});
var arm = new THREE.Mesh(armGeometry, armMaterial);
scene.add(arm);

// Create the pendulum bob
var bobGeometry = new THREE.SphereGeometry(0.5, 32, 32);
var bobMaterial = new THREE.MeshBasicMaterial({color: 0xff0000});
var bob = new THREE.Mesh(bobGeometry, bobMaterial);
scene.add(bob);

camera.position.z = 10;

var theta = Math.PI / 4;  // Initial angle
var omega = 0;  // Angular velocity
var alpha = 0;  // Angular acceleration
var g = 9.8;  // Gravitational constant
var L = 5;  // Length of pendulum

function animate() {
    requestAnimationFrame(animate);

    alpha = (-g / L) * Math.sin(theta);  // Update angular acceleration
    omega += alpha * 0.01;  // Update angular velocity
    theta += omega * 0.01;  // Update angle

    arm.rotation.z = theta;
    bob.position.set(L * Math.sin(theta), -L * Math.cos(theta), 0);  // Update bob position

    renderer.render(scene, camera);
}

animate();
