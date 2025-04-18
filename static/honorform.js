


function checkRace() {
    //console.log(this);
    $(".race_checkbox").each(function () {
        console.log(this.value, this.checked);
        if (this.value == "black" && !this.checked) {
            alert("If 'Black / African American is not checked, do not proceed with this form.");
        }
    })
}

function checkType2Diabetic() {
    if (this.value == "yes") {
        $("#dq_type2diabetic").show();
    } else {
        $("#dq_type2diabetic").hide();
    }
}

function checkGender() {
    console.log(this);
    if (this.value == "female") {
        $("#dq_gender").show();
    } else {
        $("#dq_gender").hide();
    }
}

function checkSoughtTreatment() {
    console.log(this);
    if (this.value == "yes") {
        $("#dq_soughttreatment").show();
    } else {
        $("#dq_soughttreatment").hide();
    }
}

function onPageLoad() {
    //var cbs = document.querySelectorAll(".race_checkbox");
    $(".race_checkbox").on("click", checkRace);

    $(".dq_type2diabetic").on("click", checkType2Diabetic);

    $(".dq_gender").on("click", checkGender);

    $(".dq_soughttreatment").on("click", checkSoughtTreatment);


    $(".dependent_questions").hide();
}



$(window).on("load", onPageLoad);