import React, { useState, useEffect } from "react";
import { connect, useSelector, useDispatch } from "react-redux";
import { Button, Form, Label, Dropdown } from "semantic-ui-react";
import axios from "axios";
import PropTypes from "prop-types";
import { addPost } from "../../../actions/posts";
import { getUser } from "../../../actions/auth";
import { getTopics } from "../../../actions/topics";

function PostForm() {
    const [title, setTitle] = useState("");
    const [content, setContent] = useState("");
    const [topic, setTopic] = useState([]);
    const author = useSelector((state) => state.auth.user);
    const topics = useSelector((state) => state.topics.topics);
    const options = topics.map((topic) => ({
        key: topic.name,
        text: topic.name,
        value: topic.id,
    }));

    const genderOptions = [
        { key: "m", text: "Male", value: "male" },
        { key: "f", text: "Female", value: "female" },
        { key: "o", text: "Other", value: "other" },
    ];
    const dispatch = useDispatch();

    useEffect(() => {
        dispatch(getTopics());
    }, [dispatch]);

    const onSubmit = (e) => {
        e.preventDefault();
        const post = {
            title: title,
            content: content,
            author: author.id,
            topics: topic,
        };
        dispatch(addPost(post));
        setTitle("");
        setContent("");
        setTopic([]);
    };

    return (
        <Form onSubmit={onSubmit}>
            <Form.Input
                required
                label="Title"
                id="title"
                value={title}
                onChange={(e) => setTitle(e.target.value)}
            />
            <Form.TextArea
                required
                label="Content"
                id="content"
                value={content}
                onChange={(e) => setContent(e.target.value)}
            />
            <Form.Dropdown
                fluid
                multiple
                selection
                placeholder="Topics"
                label="Topics"
                options={options}
                value={topic}
                onChange={(e, { value }) => setTopic(value)}
            />

            <Button
                content="Add Post"
                labelPosition="left"
                icon="edit"
                primary
            />
        </Form>
    );
}

export default PostForm;
