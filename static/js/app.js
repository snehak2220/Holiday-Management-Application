// ISO 3166-1 alpha-2 Country Codes
const countries = {
    "US": "United States",
    "IN": "India",
    "GB": "United Kingdom",
    "CA": "Canada",
    "AU": "Australia",
    "FR": "France",
    "DE": "Germany",
    "JP": "Japan",
    "CN": "China",
    "BR": "Brazil"
};
document.addEventListener('DOMContentLoaded', function() {
    document.addEventListener('click', function(event) {
        if (event.target.classList.contains('details-btn')) {
            const name = event.target.getAttribute('data-name');
            const date = event.target.getAttribute('data-date');
            const type = event.target.getAttribute('data-type');
            const description = event.target.getAttribute('data-description') || "No description available.";

            // Update modal content
            document.getElementById('modalHolidayName').textContent = name;
            document.getElementById('modalHolidayDate').textContent = date;
            document.getElementById('modalHolidayType').textContent = type;
            document.getElementById('modalHolidayDescription').textContent = description;
        }
    });
});

// Populate Country Dropdown
const countryDropdown = document.getElementById("country");
Object.entries(countries).forEach(([code, name]) => {
    const option = document.createElement("option");
    option.value = code;
    option.text = name;
    countryDropdown.add(option);
});

// Search Button Click Event
$('#searchButton').on('click', function() {
    let country = $('#country').val();
    let year = $('#year').val();
    let month = $('#month').val();
    let holidayType = $('#holidayType').val();
    let name = $('#name').val().toLowerCase();
    let date = $('#date').val();
    console.log("Selected Date:", date);
    let date = $('#date').val();
    if (date) {
        date = new Date(date).toISOString().split('T')[0];  // Format to YYYY-MM-DD
    }


    // Show loading spinner
    $('#holidaysList').html('<div class="spinner-border text-primary" role="status"><span class="visually-hidden">Loading...</span></div>');

    // Build query params
    let queryParams = `?country=${country}&year=${year}`;
    if (month) queryParams += `&month=${month}`;
    if (type) queryParams += `&type=${type}`;
    if (name) queryParams += `&name=${name}`;
    if (date) queryParams += `&date=${date}`;

    // AJAX Request
    $.ajax({
        url: `/${queryParams}`,
        method: 'GET',
        success: function(data) {
            let html = '';
            if (data.holidays.length > 0) {
                data.holidays.forEach(holiday => {
                    html += `
                    <div class="col-md-4 mb-4">
                        <div class="card h-100 shadow-sm">
                            <div class="card-body">
                                <h5 class="card-title">${holiday.name}</h5>
                                <p class="card-text">${holiday.date.iso}</p>
                                <button class="btn btn-info details-btn"
                                    data-name="${holiday.name}"
                                    data-date="${holiday.date.iso}"
                                    data-type="${holiday.type}"
                                    data-description="${holiday.description || 'No description available.'}"
                                    daindex.htmlta-bs-toggle="modal"
                                    data-bs-target="#holidayModal">
                                    Details
                                </button>
                            </div>
                        </div>
                    </div>`;
                });
            } else {
                html = '<p class="text-center">No holidays found.</p>';
            }
            $('#holidaysList').html(html);
        }
    });
});
