var backlink = "E_LSiKJXFZs"
var total = 0
var tablee = document.getElementById("tablee")

async function UrlExists(url, name) {
    // console.log(name)
    // res = await fetch("https://thingproxy.freeboard.io/fetch/"+url);
    // var stat = (res.status>199 && res.status<300)
    var stat = true
    tableDIV = document.getElementById("tableDIV")
    if(stat) {
        total += 1
        tablee = document.getElementById("tablee")
        var row = tablee.insertRow(1)
        var cellname = row.insertCell(0)
        var cellurl = row.insertCell(0)
        cellname.innerHTML = name
        cellurl.innerHTML = `<a href="${url}" target="_blank" rel="noopener noreferrer">${url}</a>`
    }
}

async function codimg() {
    res = await fetch("links.json");
    arr = []
    jsonData = await res.json();
    jsonData.forEach(element => {
        regex = new RegExp(element["regex"])
        if (regex.test(backlink)) {
            arr.push({"url":element["url"].replace("$URL", backlink),"name":element["type"]})
           }
        }
    );
    if(arr.length==0) {
        document.getElementById("tableDIV").innerHTML = `<h3 id="MATCHES">0 Matches Found</h3>`+tableDIV.innerHTML
    }
    return(arr)
}

async function start() {
    total = 0;
    document.getElementById("tableDIV").innerHTML = `
    <table id="tablee">
                <thead>
                    <tr>
                        <th>Domain</th>
                        <th>url</th>
                    </tr>
                </thead>
            </table>
            `
    console.log("STARTED")
    codimg().then((arr) => {
        arr.forEach(async (element) => {
            await UrlExists(element["url"],element["name"])
            if(!!document.getElementById("MATCHES")) {
                document.getElementById("MATCHES").innerHTML = `${total} Matches Found`
            }else {
                document.getElementById("tableDIV").innerHTML = `<h3 id="MATCHES">1 Match Found</h3>`+tableDIV.innerHTML
            }
        })
        console.log("YEAH")
    })
}

document.getElementById("mybtn").onclick=async ()=>{
    backlink = document.getElementById("txt").value
    await start();
};