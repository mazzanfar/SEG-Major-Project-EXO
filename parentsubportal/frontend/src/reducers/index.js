import { combineReducers } from "redux";
import topics from "./topics";
import posts from "./posts";
import comments from "./comments";
import resources from "./resources";
import auth from "./auth";
import ratings from "./ratings";
import pdfs from "./pdfs";
import videos from "./videos";
import children from "./children";
import disabilities from "./disabilities";

export default combineReducers({
    comments,
    children,
    posts,
    topics,
    ratings,
    auth,
    pdfs,
    videos,
    resources,
    disabilities,
});
