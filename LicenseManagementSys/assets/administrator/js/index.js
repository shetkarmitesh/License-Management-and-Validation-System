let menuicn = document.querySelector(".menuicn");
let nav = document.querySelector(".navcontainer");

menuicn.addEventListener("click", () => {
    nav.classList.toggle("navclose");
})
async function updateStatus(newStatus) {
    const label = document.querySelector('.t-op-nextlvl.label-tag');
    label.textContent = newStatus.charAt(0).toUpperCase() + newStatus.slice(1);

    try {
        const response = await fetch('/administrator/updatestatus/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken // Use the token from the script
            },
            body: JSON.stringify({ status: newStatus })
            
        });
        console.log("AAAAAAAAAAAAAAAAaaa"+response);
        
        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(`Network response was not ok: ${errorData.error}`);
        }

        const data = await response.json();
        console.log(data+"xxxxxxxxxxxxx");
        
        console.log(data); // Handle response if needed
    } catch (error) {
        console.error('Error updating status:', error);
    }
}
