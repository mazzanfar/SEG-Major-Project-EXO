import axios from 'axios'

import {RATE_POST} from './types';


axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';

// GET POSTS
export const ratePost = (ratePost) => dispatch => {
    axios
        .post('/api/ratings/', like)
        .then(res => {
            dispatch({
                type: RATE_POST,
                payload: res.data
            });
        }).catch(err => console.log(err));
};
