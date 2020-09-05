let x = 0;
let y = 0;
let s = 64;
let slashes = [];

function setup(){
  createCanvas($(document).width(), $(document).height());
  background(248);

  stroke(181, 17, 81);
  drawPattern();
}

function draw(){
  background(248);

  for (let i = 0; i < slashes.length; i++) {
    slashes[i].draw();

    if(slashes[i].updating){
      slashes[i].update();
    }
  }

  if (frameCount % 5 == 0) {
    let rand = floor(random(slashes.length));
    slashes[rand].updating = true;
    slashes[rand].speed = [0.05, -0.05][floor(random(2))];
  }
}

function drawPattern(){
  slashes = [];
  x = 0;
  y = 0;
  while (true) {
    slashes.push(new Slash(round(random(1)), x, y));

    x += s;
    if (x > width){
      x = 0;
      y += s;
    }
    if(y > height){
      break;
    }
  }
}

function windowResized() {
   resizeCanvas(10, 10);
   resizeCanvas($(document).width(), $(document).height());
   drawPattern();
}

class Slash{
  constructor(orientation, x, y){
    this.orientation = orientation;
    this.updating = false;
    this.speed = 0.05;
    this.x = x;
    this.y = y;
    this.a = 0;
    if(this.orientation){
      this.a = PI/2;
    }
    this.prevA = this.a;
  }

  draw(){
    push();
      translate(this.x + (s/2), this.y + (s/2));
      rotate(this.a);
      line(-s/2, -s/2, s/2, s/2);
    pop();
  }

  update(){
    this.a += this.speed;
    if(this.a - this.prevA > PI/2 || this.a - this.prevA < -PI/2){
      this.a = (this.orientation+1) * PI/2;
      this.orientation = !this.orientation;
      this.prevA = this.a;
      this.updating = false;
    }
  }
}
