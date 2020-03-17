import axios from 'axios'

import {LIKE_POST} from './types';


axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';

// GET POSTS
export const likePost = (like) => dispatch => {
    axios
        .post('/api/likes/', like)
        .then(res => {
            dispatch({
                type: LIKE_POST,
                payload: res.data
            });
        }).catch(err => console.log(err));
};
