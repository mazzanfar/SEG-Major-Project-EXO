import { combineReducers } from "redux";
import topics from "./topics";
import posts from "./posts";
import comments from "./comments";
import resources from "./resources";
import auth from "./auth";
import ratings from "./ratings";
import pdfs from "./pdfs";
import videos from "./videos";

export default combineReducers({
    comments,
    posts,
    topics,
    ratings,
    auth,
    pdfs,
    videos,
    resources,
});
