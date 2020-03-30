import React, { Component } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { addPost } from "../../../actions/posts";

function PostPage(props) {
    const postId = props.match.params.postId

    return (
        <h1>postId</h1>
    );
}

export default PostPage
