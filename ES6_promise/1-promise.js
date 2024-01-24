export default function getResponseFromAPI(success) {
  return new Promise((ok, ko) => {
    if (success) {
      ok({ status: 200, body: 'Success' });
    }
    ko(new Error('The fake API is not working currently'));
  });
}
