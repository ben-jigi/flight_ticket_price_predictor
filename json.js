// Mapping names to encoded numbers
const airlineMap = {
    'IndiGo': 0, 'Air India': 1, 'Jet Airways': 2, 'SpiceJet': 3,
    'Multiple carriers': 4, 'GoAir': 5, 'Vistara': 6, 'Air Asia': 7,
    'Vistara Premium economy': 8, 'Jet Airways Business': 9,
    'Multiple carriers Premium economy': 10, 'Trujet': 11
};

const sourceMap = { 'Banglore':0, 'Kolkata':1, 'Delhi':2, 'Chennai':3, 'Mumbai':4 };
const destinationMap = { 'New Delhi':0, 'Banglore':1, 'Cochin':2, 'Kolkata':3, 'Delhi':4, 'Hyderabad':5 };

function makePrediction() {
    const data = {
        Airline: airlineMap[document.getElementById("Airline").value],
        Source: sourceMap[document.getElementById("Source").value],
        Destination: destinationMap[document.getElementById("Destination").value],
        Total_Stops: parseInt(document.getElementById("Total_Stops").value),
        journey_day: parseInt(document.getElementById("journey_day").value),
        journey_month: parseInt(document.getElementById("journey_month").value),
        weekday_num: parseInt(document.getElementById("weekday_num").value),
        journey_hour: parseInt(document.getElementById("journey_hour").value),
        journey_minute: parseInt(document.getElementById("journey_minute").value),
        durations: parseInt(document.getElementById("durations").value)
    };

    fetch("/predict", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);  // debug
        document.getElementById("result").innerText = "Predicted Flight Price: ₹" + data.prediction;
    })
    .catch(error => console.error('Error:', error));
}
