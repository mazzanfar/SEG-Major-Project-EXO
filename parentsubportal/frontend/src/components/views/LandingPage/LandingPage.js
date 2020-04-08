import React, { Fragment } from "react";
import BlogPosts from "./BlogPosts";
import { useDispatch } from "react-redux";
import PostForm from "./PostForm";
import Test from "./TestComponent";
import { getUser } from "../../../actions/auth";

export default function LandingPage() {
    const dispatch = useDispatch();
    dispatch(getUser());
    return (
        <Fragment>
            <PostForm />
            <BlogPosts />
        </Fragment>
    );
}
