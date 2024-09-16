// Check if Three.js is loaded
if (typeof THREE !== 'undefined') {
    // Create a scene
    var scene = new THREE.Scene();
    var camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);

    // Create a renderer and attach it to the #simulation-container
    var renderer = new THREE.WebGLRenderer();
    renderer.setSize(window.innerWidth, window.innerHeight);
    document.getElementById('simulation-container').appendChild(renderer.domElement);

    // Handle window resize
    window.addEventListener('resize', function() {
        var width = window.innerWidth;
        var height = window.innerHeight;
        renderer.setSize(width, height);
        camera.aspect = width / height;
        camera.updateProjectionMatrix();
    });

    // Create the ground
    var groundGeometry = new THREE.PlaneGeometry(500, 500);
    var groundMaterial = new THREE.MeshBasicMaterial({color: 0x228B22, side: THREE.DoubleSide});
    var ground = new THREE.Mesh(groundGeometry, groundMaterial);
    ground.rotation.x = Math.PI / 2;
    ground.position.y = 0;  // Ensure it's at y=0
    scene.add(ground);

    // Create a ball for projectile motion
    var ballGeometry = new THREE.SphereGeometry(1, 32, 32);
    var ballMaterial = new THREE.MeshBasicMaterial({color: 0xff0000});
    var ball = new THREE.Mesh(ballGeometry, ballMaterial);
    ball.position.set(0, 2, 0); // Start a bit above the ground
    scene.add(ball);

    // Lighting
    var light = new THREE.PointLight(0xFFFFFF, 1, 500);
    light.position.set(10, 50, 50);
    scene.add(light);

    // Set the camera position
    camera.position.z = 50;

    // Initial velocities and physics parameters
    var velocityX = 2;  // Horizontal velocity
    var velocityY = 5;  // Vertical velocity (initial upward motion)
    var gravity = -9.81;  // Gravity acceleration (negative for downward)
    var timeStep = 0.05;  // Time increment per frame

    // Animate the ball (basic projectile motion simulation)
    function animate() {
        requestAnimationFrame(animate);

        // Apply gravity to vertical velocity
        velocityY += gravity * timeStep;

        // Update ball position
        ball.position.x += velocityX * timeStep;
        ball.position.y += velocityY * timeStep;

        // Reset ball if it hits the ground
        if (ball.position.y <= 0) {
            ball.position.y = 0;   // Ball stays on the ground
            velocityY = 5;         // Reset vertical velocity for next bounce
        }

        // Render the scene
        renderer.render(scene, camera);
    }

    // Start animation
    animate();
}
else {
    console.error('Three.js library is not loaded.');
}
