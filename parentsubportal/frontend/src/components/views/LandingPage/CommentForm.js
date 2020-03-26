import React, { Component, useState } from "react";
import axios from "axios";
import { Button, Form, Message } from "semantic-ui-react";
import { postComment } from "../../../actions/comments";
import { useSelector, useDispatch } from "react-redux";

axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFToken";

function CommentForm(props) {
    const [content, setContent] = useState("");
    const author = useSelector((state) => state.auth.user);
    const dispatch = useDispatch();

    const handleSubmit = (e) => {
        e.preventDefault();
        const comment = {
            post: props.post.id,
            content: content,
            author: author.id,
        };
        dispatch(postComment(comment));
    };

    return (
        <Form reply onSubmit={handleSubmit}>
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

export default CommentForm;
