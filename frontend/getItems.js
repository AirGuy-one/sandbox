function fetchPortfolioData(url, method, body = null) {
  fetch(url, {
    method: method,
    headers: {
      'Content-Type': 'application/json'
    },
    body: body
  })
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .then(data => {
      console.log('Response:', data);
    })
    .catch(error => {
      console.error('Error fetching data:', error);
    });
}

fetchPortfolioData(
    'http://localhost:8000/api/v1/feedback/create_callback_query/',
    'POST',
    JSON.stringify({
        "phone_number": "+79109277743",
        "name": "Billy"
    })
);
