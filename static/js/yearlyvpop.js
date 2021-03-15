let select = d3.select("select");
//import data

//insert data into HTML for view upon opening page
data.forEach(({county}) =>{
    let option = select.append(`option value= ${value}`).text(county);
});
