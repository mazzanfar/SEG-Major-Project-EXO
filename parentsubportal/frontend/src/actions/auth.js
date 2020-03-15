import axios from 'axios';

import { GET_USER } from './types';

// GET USER
export const getUser = () => dispatch => {
    axios
    .get(`/api/auth/user`)
    .then(res => {
        dispatch( {
            type: GET_USER,
            payload: res.data,
        });
    })
    .catch(err => console.log(err));
}
