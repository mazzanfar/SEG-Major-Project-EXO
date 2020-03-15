import {combineReducers} from 'redux';
import topics from './topics';
import posts from './posts'
import comments from './comments'
import documents from './documents'
import auth from './auth'
import ratings from './ratings'

export default combineReducers({
    posts,
    topics,
    documents,
    comments,
    ratings,
    auth,
});
