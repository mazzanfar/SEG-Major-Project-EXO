import axios from 'axios';

import { GET_DOCUMENTS } from './types';

// GET DOCUMENTS
export const getDocuments = () => dispatch => {
    axios
    .get('/api/documents/')
    .then(res => {
        dispatch({
            type: GET_DOCUMENTS,
            payload: res.data
        });
    }).catch(err => console.log(err));
};
