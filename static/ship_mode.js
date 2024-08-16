setFullscreen();

let resultIslands = [];

let camera = 0;

for (let i = 0; i < results.length; i++){
  resultIslands.push({ x: 0, y: i * (50 + 291/2) + 100 + 291/2, title: results[i].title, href: results[i].href });
}

let island = tryToLoad("island", "sand"),
  tile_water = tryToLoad("tile_water", "blue");

function update() {
  camera += 1;
}

function draw() {
  resultIslands.forEach(drawResult);
}

function keyup(key) {

}

function mouseup() {

}

function drawResult(resultIsland) {
  drawImage(island, resultIsland.x, resultIsland.y - camera, 412 / 2, 291 / 2);
  context.font = '24px "PT Sans"';
  context.fillStyle = "red";
  context.fillText(resultIsland.title, resultIsland.x, resultIsland.y - camera + 24, 412 / 2);
}
