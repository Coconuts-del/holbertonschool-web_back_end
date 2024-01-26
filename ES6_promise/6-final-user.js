import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName = '', lastName = '', fileName = '') {
  return Promise.allSettled([
    uploadPhoto(fileName).then((result) => ({
      status: result.status,
      value: result.status === 'fulfilled' ? result.value : String(result.reason),
    })),
    signUpUser(firstName, lastName).then((result) => ({
      status: result.status,
      value: result.status === 'fulfilled' ? result.value : String(result.reason),
    })),
  ]);
}
