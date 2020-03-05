import { combineReducers } from 'redux';
import topics from './topics';
import posts from './posts'
import comments from './comments'
import documents from './documents'
import auth from './auth'

export default combineReducers({
    posts,
    topics,
    documents,
    comments,
    auth
});
