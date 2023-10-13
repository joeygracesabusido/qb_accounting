// this function is for inserting balance sheet type

const insert_balance_sheet_type_1 = async () => {
    const data = {
      bs_type: document.querySelector('#bs_type_insert1').value
    }
 
    console.log(data)
 
    if (data.bs_type == ''){
     window.alert("Please fill up input fields")
    } else {
     try {
         const response = await fetch(`/api-insert-balance-sheet-type`,{
             method: "POST",
             headers: { "Content-Type": "application/json" },
             body: JSON.stringify(data)
         });
 
         // Check if the response was successful
         if (response.status === 200) {
             window.alert("Your data has been saved");
             
             window.location.assign("/dashboard/");
         } else if (response.status === 401) {
             window.alert("Unauthorized credential. Please login");
         }
     } catch (error) {
         // Catch any errors and log them to the console
         window.alert(error);
        
     }
    }
 }
 
 // Attach the event listener to the button
 var Btn_save_bs_class = document.querySelector('#Btn_save_bs_class');
 Btn_save_bs_class.addEventListener("click", insert_balance_sheet_type_1);