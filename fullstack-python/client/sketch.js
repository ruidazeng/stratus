let test;

function setup() {
  let cnv = createCanvas(200, 200);
  background(0)

  cnv.parent('drawing');

  user_digit = createGraphics(200, 200)
  user_digit.pixelDensity(1)
}

function draw() {
  image(user_digit, 0, 0)
  if (test) {
    image(test, 0, 0)
  }
}

function mouseDragged() {
  user_digit.stroke(255)
  user_digit.strokeWeight(14)
  user_digit.line(mouseX, mouseY, pmouseX, pmouseY)
}

function keyPressed() {
  if (key == ' ') {
    user_digit.background(0)
  }
}

function mouseReleased() {
  let data = guessUserDigit()

  $.ajax({
    type: "POST",
    url: "https://mnistonline.herokuapp.com/predict/",
    data: {
      'arr': JSON.stringify(data)
    },
    success: function(result) {
      $("#prediction").html(result)
    },
  });
}

function guessUserDigit() {
  let img = user_digit.get()
  let inputs = []
  img.resize(28, 28)
  img.loadPixels()

  for (let i = 0; i < 784; i++) {
    inputs[i] = img.pixels[i * 4]
  }

  test = img
  return inputs
}