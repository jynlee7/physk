// lens_optics_3d.js

var scene = new THREE.Scene();
var camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
var renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

// Create a lens (as a transparent cylinder)
var lensGeometry = new THREE.CylinderGeometry(2, 2, 1, 32);
var lensMaterial = new THREE.MeshBasicMaterial({color: 0x00ff00, opacity: 0.5, transparent: true});
var lens = new THREE.Mesh(lensGeometry, lensMaterial);
lens.rotation.z = Math.PI / 2;
scene.add(lens);

// Create a light ray (as a line)
var rayGeometry = new THREE.Geometry();
rayGeometry.vertices.push(new THREE.Vector3(-10, 0, 0));
rayGeometry.vertices.push(new THREE.Vector3(10, 0, 0));
var rayMaterial = new THREE.LineBasicMaterial({color: 0xffffff});
var ray = new THREE.Line(rayGeometry, rayMaterial);
scene.add(ray);

camera.position.z = 10;

function animate() {
    requestAnimationFrame(animate);

    // Basic animation of ray direction change through lens (for illustration)
    ray.rotation.z += 0.01;

    renderer.render(scene, camera);
}

animate();
