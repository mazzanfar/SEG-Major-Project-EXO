import axios from 'axios';

import { GET_COMMENTS, POST_COMMENT } from './types';

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';

// GET COMMENTS
export const getComments = id => dispatch => {
    /*
    axios
    .get(`/api/posts/${id}/`)
    .then(res => {
        dispatch( {
            type: GET_COMMENTS,
            payload: id
        })
    })
    .catch(err => console.log(err));
    */
}

// POST COMMENT 
export const postComment = (comment) => dispatch => {
    axios
    .post('/api/comments/', comment)
    .then(res => {
        dispatch({
            type: POST_COMMENT,
            payload: res.data
        });
    }).catch(err => console.log(err));
};
