let test;

// we can just make an array of previous predictions
let composition = [] 

function setup() {
  let cnv = createCanvas(200, 200);
  background(0)

  cnv.parent('drawing');

  user_digit = createGraphics(200, 200)
  user_digit.pixelDensity(1)
}

function draw() {
  image(user_digit, 0, 0)
  // if (test) {
  //   image(test, 0, 0)
  // }
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

function clearViaButton() {
  user_digit.background(0)
}


function clearPrediction() {
  $("#prediction").html("Please Input A Number")
  clearGraph() 
  clearViaButton()
}

function predictText() {
  let data = guessUserDigit()

  console.log(typeof(JSON.stringify(data)))

  $.ajax({
    type: "POST",
    url: "http://129.114.26.3:30005/predict",
    data: {
      'image': JSON.stringify(data)
    },
    success: function(result) {
      let getCurrentData = document.querySelector('#prediction').innerHTML

      // console.log(JSON.parse(result.prediction).Answer)

      if (getCurrentData == "Please Input A Number") {
        // we can skip this
        $("#prediction").html(JSON.parse(result.prediction).Answer)
      } else {
        $("#prediction").html(getCurrentData + " " + JSON.parse(result.prediction).Answer)
      }

      // list out in a graph 
      graphPrediction(JSON.parse(result.prediction).Prob)
    },
  });
}

function graphPrediction(graphArray) {
  // console.log(graphArray)
  // replace the data there: (at first its all zeros)
  myChart.data.datasets[0].data = graphArray
  myChart.update()
}

function clearGraph() {
  myChart.data.datasets[0].data = [0,0,0,0,0,0,0,0,0]
  myChart.update()
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