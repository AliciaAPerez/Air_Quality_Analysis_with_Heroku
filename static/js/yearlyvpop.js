// let select = d3.select("select");
// //import data

// //insert data into HTML for view upon opening page
// data.forEach(({county}) =>{
//     let option = select.append(`option value= ${value}`).text(county);
// });

// option = select.append(`option value= ${value}`).text(county);
// select.append(`option value= ${value}`).text(county);

$("#selDataset").on("change", function runFilter() {
    d3.event.preventDefault();


    // d3.csv("getPlotCSV").then(function(saqiData) {
    //     console.log(saqiData)
    // });

    var yearValue = []

    d3.csv("getPlotCSV").then(function(saqiData) {


        const data = saqiData;
        console.log(data)

        for (let [value] of Object.entries(data)) {
            for (let index = 0; index < data.length; index++) {
                const aqiData = data[index];

                var yearValue = aqiData.year.append()
            
                var yearValue = document.getElementById("year").value;
            // var cityValue = document.getElementById("city").value.toLowerCase();
            // var stateValue = document.getElementById("state").value.toLowerCase();
            // var countryValue = document.getElementById("country").value.toLowerCase();
            // var shapeValue = document.getElementById("shape").value.toLowerCase();

            
            
            var filteredData = tableData;
        //Fitler each search criteria
            if (dateValue !== ""){
                filteredData = filteredData.filter(data => data.datetime === dateValue);
            }

    // Get a reference to the table body
            var tbody = d3.select("tbody");
            tbody.html("");
            }
        }
    });
});

