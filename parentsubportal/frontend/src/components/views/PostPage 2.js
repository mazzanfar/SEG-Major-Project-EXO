import React, { Component, useEffect } from "react";
import { connect, useDispatch, useSelector } from "react-redux";
import PropTypes from "prop-types";
import { getPost } from "../../actions/posts";
import PostDetail from "./LandingPage/PostDetail";
import { Item } from "semantic-ui-react";

function PostPage(props) {
    const postId = props.match.params.postId;
    const post = useSelector((state) => state.posts.post);
    const dispatch = useDispatch();

    useEffect(() => {
        dispatch(getPost(postId));
    }, [dispatch]);

    return post ? (
        <Item.Group>
            <PostDetail post={post} />
        </Item.Group>
    ) : null;
}
export default PostPage;
