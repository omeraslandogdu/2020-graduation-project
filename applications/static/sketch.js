const checkList = [];
let capture, canvas, classifier, foundPerson, label;

function setup() {
    canvas = createCanvas(320, 260);
    canvas.parent('myCanvas');

    capture = createCapture(VIDEO);
    capture.size(width, height);
    capture.hide();

    classifier = ml5.imageClassifier('https://teachablemachine.withgoogle.com/models/FlPDCUsQ/model.json');

    setInterval(function () {
        findPerson(capture);
    }, 250);
}

function draw() {
    background(0);
    image(capture, 0, 0);
    fill(255);
    textSize(16);
    textAlign(CENTER);
    text(label, width / 2, height - 4);
}

function findPerson(flippedImage) {
    classifier.classify(flippedImage, function (error, results) {
        if (error) return console.error(error);

        foundPerson = results[0];
        label = foundPerson ? foundPerson.label : 'Lütfen yüzünüzü yaklaştırınız';
        if (foundPerson.confidence < 0.95) {
            foundPerson = null;

            return;
        }

        if (checkList.indexOf(foundPerson.label) === -1) {
            checkList.push(foundPerson.label);

            $.ajax({
                type: "POST",
                url: "/yoklama-al",
                data: {
                    personId: foundPerson.label
                },
                success: function () {
                    label = 'Yoklamanız alındı!';
                }, error: function () {
                    label = 'Veritabanına alınırken hata oluştu!';
                }
            });
        }
    });
}