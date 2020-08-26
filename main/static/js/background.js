let x = 0;
let y = 0;
let s = 40;
let count = 0;
let slashes = [];

function setup(){
  createCanvas($(document).width(), $(document).height());
  background(248);

  stroke(156, 15, 117);
  drawPattern();
}

function draw(){
  background(248);

  for (let i = 0; i < slashes.length; i++) {
    slashes[i].draw();
  }

  for (let i = 0; i < slashes.length; i++) {
    if(slashes[i].updating){
      slashes[i].update();
    }
  }

  if (frameCount % 5 == 0) {
    slashes[floor(random(slashes.length))].updating = true;
  }
}

function drawPattern(){
  slashes = [];
  for (let i = 0; i < width/s; i++) {
    for (let j = 0; j < height/s; j++) {
      slashes.push(new Slash(round(random(1)), x, y));
      // if(round(random(1))){
      //   line(x, y, x + s, y + s);
      // }else{
      //   line(x, y + s, x + s, y);
      // }

      x += s;
      if (x > width){
        x = 0;
        y += s;
      }
      if(y > height){
        y = 0;
      }
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
    this.a += 0.05;
    if(this.a - this.prevA > PI/2){
      this.a = (this.orientation+1) * PI/2;
      this.orientation = !this.orientation;
      this.prevA = this.a;
      this.updating = false;
    }
  }
}
