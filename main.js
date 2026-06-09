form=document.getElementById("predictionForm")

async function Model(event){
    // we set this here to prevent the refresh because the refresh will wait untill this function be full implement
    event.preventDefault();
    // place of presenting the model response
    const predictionValue = document.getElementById("predictionValue");
    const resultBox = document.getElementById("resultBox");
    // prepare the data 
    const formData={
        Age:parseFloat(document.getElementById("Age").value),
        Height:parseFloat(document.getElementById("Height").value),
        Weight:parseFloat(document.getElementById("Weight").value),
        Sprint_40yd:parseFloat(document.getElementById("Sprint_40yd").value),
        Vertical_Jump:parseFloat(document.getElementById("Vertical_Jump").value),
        Bench_Press_Reps:parseFloat(document.getElementById("Bench_Press_Reps").value),
        Broad_Jump:parseFloat(document.getElementById("Broad_Jump").value),
        Player_Type:document.getElementById("Player_Type").value,
        Position_Type:document.getElementById("Position_Type").value

    };
    // start talking to the API
    try{
        const response = await fetch('https://comp-gci.vercel.app/model',{
            method:"POST",
            headers: {
                "Content-Type":"application/json"
            },
            body:JSON.stringify(formData)
        });

        const data = await response.json();

        let resultText="";
        if (data.response_result ===1){
            resultText="Accepted";
        }else{
            resultText="Not Accepted";
        }

        predictionValue.innerText = resultText + " (" + data.response_proba + "%)";
        resultBox.classList.remove('hidden');
    } catch(error){
        alert("The Server Is Down")
    }
}

form.addEventListener('submit', Model);