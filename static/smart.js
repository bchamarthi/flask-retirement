function createStar(xMax, yMax) {
  const size = math.randomInt(1, 4);

  const star = {
    x: math.randomInt(5, xMax),
    y: math.randomInt(5, yMax),
    name: size.toString(),
    size,
  };

  return star;
}

function drawStar(context, star) {
  context.beginPath();
  context.arc(star.x, star.y, star.size, 0, 2 * Math.PI);
  context.shadowColor = '#e6e6e6';
  context.shadowBlur = 4;
  context.fillStyle = '#e6e6e6';
  context.fill();
}

const canvas = document.getElementById('stars');
const context = canvas.getContext('2d');
let start = Date.now();
let stars;

const handleResize = () => {
  const { innerWidth, innerHeight } = window;
  canvas.width = innerWidth;
  canvas.height = innerHeight;

  stars = [];

  for (let i = 0; i < 100; i++) {
    const star = createStar(innerWidth, innerHeight);

    stars.push(star);

    drawStar(context, star);
  }
};

window.addEventListener('resize', handleResize);
handleResize();

const animate = () => {
  const { innerWidth, innerHeight } = window;
  requestAnimationFrame(animate);

  const time = Date.now();
  const delta = (start - time) * -0.08;
  start = time;

  context.clearRect(0, 0, innerWidth, innerHeight);

  for (let i = 0; i < 100; i++) {
    stars[i].x += delta * parseInt(stars[i].name, 10) * 0.2;
    if (stars[i].x > innerWidth) stars[i] = createStar(0, innerHeight);

    drawStar(context, stars[i]);
  }
};

animate();