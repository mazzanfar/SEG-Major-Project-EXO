import React, { Component, Fragment, useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Item } from "semantic-ui-react";
import axios from "axios";
import PropTypes from "prop-types";
import PostDetail from "./PostDetail";
import { getPosts } from "../../../actions/posts";
import Comments from "./Comments";

function BlogPosts() {
    const dispatch = useDispatch();
    const posts = useSelector((state) => state.posts.posts);

    useEffect(() => {
        dispatch(getPosts());
    }, [dispatch]);

    return (
        <Fragment>
            <br />
            {posts.map((post) => (
                <Item.Group>
                    <PostDetail post={post}></PostDetail>
                    <Comments post={post} />
                </Item.Group>
            ))}
        </Fragment>
    );
}

export default BlogPosts;
