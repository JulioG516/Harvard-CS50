function calculateMacro(){
    // Setting Variables to get Formula
    let age = parseInt(document.getElementById("formGroupAge").value);
    let height = parseInt(document.getElementById("formGroupHeight").value);
    let weight = parseInt(document.getElementById("formGroupWeight").value);
    let goal = parseInt(document.getElementById("selectGoal").value);
    let activity;
    var ele = document.getElementsByName('radioActivity');

    for(i = 0; i < ele.length; i++) {
        if(ele[i].checked)
        {
            activity = parseInt(ele[i].value);
        }
    }


    let BMR;
    let activityLevel;

    switch (activity) {
        case 1:
            activityLevel = 1.2;
            break;
        case 2:
            activityLevel = 1.375;
            break;
        case 3:
            activityLevel = 1.550;
            break;
        case 4:
            activityLevel = 1.725;
            break;
        case 5:
            activityLevel = 1.9;
            break;
        default:
            activityLevel = 1.2;
            break;
    }


    if(document.getElementById('male').checked)
    {

        BMR = (10 * weight) + (6.25 * height) - (5 * age)  + 5;
        BMR = Math.round(BMR * activityLevel);

        switch (goal){
            case 1:
                break;
            case 2:
                percentage = Math.round(BMR * 10 / 100);
                BMR = Math.round(BMR - percentage);
                break;
            case 3:
                BMR += 500;
        }

    }
    else if(document.getElementById('female').checked)
    {

        BMR = (10 * weight) + (6.25 * height) - (5 * age)  + 161;
        BMR = Math.round(BMR * activityLevel);


        switch (goal){
            case 1:
                break;
            case 2:
                percentage = Math.round(BMR * 10 / 100);
                BMR = Math.round(BMR - percentage);
                break;
            case 3:
                BMR += 500;
        }
    }
    const basal = BMR;
    let carbo;
    let protein;
    let fat;

    switch (goal)
    {
        case 1: // Mantain Gain
            carbo =  Math.round(basal * 40 / 100);
            protein =  Math.round(basal * 30 / 100);
            fat =  Math.round(basal * 30 / 100);
            break;
        case 2: // Weight Loss
            carbo =  Math.round(basal * 40 / 100);
            protein =  Math.round(basal * 40 / 100);
            fat =  Math.round(basal * 20 / 100);
            break;
        case 3:
            carbo =  Math.round(basal * 40 / 100);
            protein =  Math.round(basal * 30 / 100);
            fat =  Math.round(basal * 30 / 100);
            break;
        default:
            break;

    }

    let showCarbo = `Carbs: ${Math.round(carbo / 4)}g per day (${carbo} Calories.)`;
    let showProtein = `Protein: ${Math.round(protein / 4)}g per day (${protein} Calories.)`;
    let showFats= `Fats: ${Math.round(fat / 9)}g per day (${fat} Calories.)`;

    let showResult1 = document.getElementById("firstResult");
    showResult1.innerHTML = `${showCarbo} <br> ${showProtein} <br> ${showFats} <br> Total Calories: ${basal}`;

}


function calculateBMI(){
    const height = parseInt(document.getElementById("bmiHeight").value);
    const weight = parseInt(document.getElementById("bmiWeight").value);
    const bmi = (weight / ((height**2)/10000)).toFixed(2);
    let showResult1 = document.getElementById("bmiFirstResult");
    let showResultParagraph = document.getElementById("bmiParagraph");
    let showGuide = document.getElementById("bmiGuide");


    if (bmi < 18.6)
    {
        showResult1.innerHTML = `Under Weight - Your BMI: ${bmi}`;
        showResultParagraph.innerHTML = "Body mass index (BMI) is a person’s weight in kilograms divided by the square of height in meters. BMI is an inexpensive and easy screening method for weight category—underweight, healthy weight, overweight, and obesity.BMI does not measure body fat directly, but BMI is moderately correlated with more direct measures of body fat 1,2,3. Furthermore, BMI appears to be as strongly correlated with various metabolic and disease outcome as are these more direct measures of body fatness."
        showGuide.innerHTML =`BMI Weight Guide<br>
        Under Weight = Less than 18.6<br>
        Normal Range = 18.6 and 24.9<br>
        Overweight = Greater than 24.9`
    }
    else if (bmi >= 18.6 && bmi <= 24.9)
    {
        showResult1.innerHTML = `Normal range - Your BMI: ${bmi}`;
        showResultParagraph.innerHTML = "Body mass index (BMI) is a person’s weight in kilograms divided by the square of height in meters. BMI is an inexpensive and easy screening method for weight category—underweight, healthy weight, overweight, and obesity.BMI does not measure body fat directly, but BMI is moderately correlated with more direct measures of body fat 1,2,3. Furthermore, BMI appears to be as strongly correlated with various metabolic and disease outcome as are these more direct measures of body fatness."
        showGuide.innerHTML =`BMI Weight Guide<br>
        Under Weight = Less than 18.6<br>
        Normal Range = 18.6 and 24.9<br>
        Overweight = Greater than 24.9`
    }
    else if (bmi >= 24.9)
    {
        showResult1.innerHTML = `Overweight - Your BMI: ${bmi}`;
        showResultParagraph.innerHTML = "Body mass index (BMI) is a person’s weight in kilograms divided by the square of height in meters. BMI is an inexpensive and easy screening method for weight category—underweight, healthy weight, overweight, and obesity.BMI does not measure body fat directly, but BMI is moderately correlated with more direct measures of body fat. Furthermore, BMI appears to be as strongly correlated with various metabolic and disease outcome as are these more direct measures of body fatness."
        showGuide.innerHTML =`BMI Weight Guide<br>
        Under Weight = Less than 18.6<br>
        Normal Range = 18.6 and 24.9<br>
        Overweight = Greater than 24.9`
    }
}

function calculateBF(){
    const age = parseInt(document.getElementById("bfAge").value);

    let bmiMultiplier;
    let ageMultiplier;
    let sexMultiplier;
    let isMale = false;
    let isFemale = false;
    let classDescription = "";


    if (age < 15)
    {
        bmiMultiplier = 1.51;
        ageMultiplier = 0.70;
        sexMultiplier = 3.6;
    }
    else (age >= 15)
    {
        bmiMultiplier = 1.20;
        ageMultiplier = 0.23;
        sexMultiplier = 10.8;
    }
    let bf;
    const height = parseInt(document.getElementById("bfHeight").value);
    const weight = parseInt(document.getElementById("bfWeight").value);
    const bmi = (weight / ((height**2)/10000)).toFixed(2);
    let showResult1 = document.getElementById("bfFirstResult");
    let showResultParagraph = document.getElementById("bfParagraph");
    let showTable = document.getElementById("tableBF");

    if(document.getElementById('male').checked)
    {
        isMale = true;
        bf = (bmiMultiplier * bmi) + (ageMultiplier * age) - (sexMultiplier * 1) - 5.4;

    }
    else if(document.getElementById('female').checked)
    {
        isFemale = true;
        bf = (bmiMultiplier * bmi) + (ageMultiplier * age) - (sexMultiplier * 0) - 5.4;
    }

    if (isMale == true)
    {
        if (bf >= 25){
            classDescription = "Obese";
        }
        else if (bf >= 17.01 && bf <= 24)
        {
            classDescription = "Average";
        }
        else if (bf >= 14 && bf <= 17)
        {
            classDescription = "Fitness";
        }
        else if (bf >= 6 && bf <= 13)
        {
            classDescription = "Athletes";
        }
        else if (bf >= 2.5 && bf <= 5)
        {
            classDescription = "Essential fat";
        }
        else{
            classDescription = "Not Recognized";
        }
    }

    if (isFemale == true)
    {
        if (bf >= 32){
            classDescription = "Obese";
        }
        else if (bf >= 25 && bf <= 31)
        {
            classDescription = "Average";
        }
        else if (bf >= 21 && bf <= 24)
        {
            classDescription = "Fitness";
        }
        else if (bf >= 14 && bf <= 20)
        {
            classDescription = "Athletes";
        }
        else if (bf >= 10 && bf <= 13)
        {
            classDescription = "Essential fat";
        }
        else{
            classDescription = "Not Recognized";
        }
    }

    showResult1.innerHTML = `Your Body Fat Percentage: ${bf.toFixed(2)}.<br> You are on the category: ${classDescription}.`;
    showTable.innerHTML = `
    <caption >Typical Body fat amounts</caption>
    <tr><th>Description</th><th>Women</th><th>Men</th></tr>
    <tr><td>Essential fat</td><td>10-13%</td><td>2-5%</td></tr>
    <tr><td>Athletes</td><td>14-20%</td><td>6-13%</td></tr>
    <tr><td>Fitness</td><td>21-24%</td><td>14-17%</td></tr>
    <tr><td>Average</td><td>25-31%</td><td>18-24%</td></tr>
    <tr><td >Obese</td><td>32%+</td><td>25%+</td></tr>`
}
