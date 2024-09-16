// electric_field_3d.js

var scene = new THREE.Scene();
var camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
var renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

// Create charges (spheres)
var charge1Geometry = new THREE.SphereGeometry(0.5, 32, 32);
var charge1Material = new THREE.MeshBasicMaterial({color: 0xff0000});
var charge1 = new THREE.Mesh(charge1Geometry, charge1Material);
charge1.position.set(-5, 0, 0);
scene.add(charge1);

var charge2Geometry = new THREE.SphereGeometry(0.5, 32, 32);
var charge2Material = new THREE.MeshBasicMaterial({color: 0x0000ff});
var charge2 = new THREE.Mesh(charge2Geometry, charge2Material);
charge2.position.set(5, 0, 0);
scene.add(charge2);

camera.position.z = 20;

// Create field lines (for simplicity, we can animate the lines' direction)
function createFieldLines() {
    var lines = [];
    for (var i = 0; i < 10; i++) {
        var geometry = new THREE.Geometry();
        geometry.vertices.push(new THREE.Vector3(-5, 0, 0));
        geometry.vertices.push(new THREE.Vector3(5, Math.sin(i), Math.cos(i)));
        var material = new THREE.LineBasicMaterial({color: 0xffffff});
        var line = new THREE.Line(geometry, material);
        scene.add(line);
        lines.push(line);
    }
    return lines;
}

var fieldLines = createFieldLines();

function animate() {
    requestAnimationFrame(animate);

    fieldLines.forEach(function(line) {
        line.rotation.z += 0.01;
    });

    renderer.render(scene, camera);
}

animate();
