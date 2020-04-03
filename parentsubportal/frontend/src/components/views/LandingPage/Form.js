import React, { useState, Component } from "react";
import { connect, useSelector, useDispatch } from "react-redux";
import { Button, Form, Message } from "semantic-ui-react";
import axios from "axios";
import PropTypes from "prop-types";
import { addPost } from "../../../actions/posts";
import { getUser } from "../../../actions/auth";

function PostForm() {
    const [title, setTitle] = useState("");
    const [content, setContent] = useState("");
    const author = useSelector((state) => state.auth.user);
    const dispatch = useDispatch();

    const onSubmit = (e) => {
        e.preventDefault();
        console.log(author);
        const post = { title: title, content: content, author: author.id };
        dispatch(addPost(post));
    };

    return (
        <Form reply onSubmit={onSubmit}>
            <Form.TextArea
                required
                id="title"
                value={title}
                onChange={(e) => setTitle(e.target.value)}
            />
            <Form.TextArea
                required
                id="content"
                value={content}
                onChange={(e) => setContent(e.target.value)}
            />
            <Button
                content="Add Reply"
                labelPosition="left"
                icon="edit"
                primary
            />
        </Form>
    );
}

export default PostForm;
