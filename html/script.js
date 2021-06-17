function addOptions(drivers) {
    var select = document.getElementById("drivers")
    for (driver of drivers) {
        var opt = document.createElement('option');
        opt.value = driver;
        opt.innerHTML = driver;
        select.appendChild(opt);
        if (driver.toLowerCase() == document.driver_odbc) {
            opt.selected = true
        }
    }

}

data = getDataFromRB({module_name:"odbc", command_name:"get_drivers"})
.then(data => {
    drivers = data["drivers"]
    addOptions(drivers)
})

