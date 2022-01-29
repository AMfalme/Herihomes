$(
  $("#sendInquiryForm").submit(function(e) {
    e.preventDefault();
    var form = $(this);
    var data = getFormData(form);
    data.message = $("#contact_message").val();
    console.log(data);
    $.ajax({
      type: "POST",
      contentType: "application/json",
      url: "contactmessage",
      headers: {
        "X-CSRFToken": csrftoken
      },
      data: JSON.stringify(data),
      success: function(response, status) {
        if (response.error) {
          $("#sendInquiryForm").hide();
          $("#sendInquiryResponse").css("display", "block");
          $("#sendInquiryResponse").css("background-color", "red !important");
          $("#sendInquiryResponse").html(
            "<p>" +
              "Error occured, kindly contact us on the live chat on the bottom right corner" +
              "</p>"
          );
          console.log(response.error);
        } else {
          console.log("success");
          $("#sendInquiryForm").hide();
          $("#sendInquiryForm").hide();

          $("#sendInquiryResponse").html(
            "<p>" + response.error.message + "</p>"
          );
        }
      },
      error: function(response, error) {
        console.log(response);
        console.log(status);
      }
    });
  });
);