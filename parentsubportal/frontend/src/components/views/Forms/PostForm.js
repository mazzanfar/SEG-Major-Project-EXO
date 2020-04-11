import React, { useState, useEffect } from "react";
import { connect, useSelector, useDispatch } from "react-redux";
import { Button, Form, Label, Dropdown } from "semantic-ui-react";
import axios from "axios";
import PropTypes from "prop-types";
import { addPost } from "../../../actions/posts";
import { getUser } from "../../../actions/auth";
import { getTopics } from "../../../actions/topics";
import { getResources } from "../../../actions/resources";

function PostForm() {
    const author = useSelector((state) => state.auth.user);
    const topics = useSelector((state) => state.topics.topics);
    const disabilities = useSelector(
        (state) => state.disabilities.disabilities
    );
    const topicOptions = topics.map((topic) => ({
        key: topic.name,
        text: topic.name,
        value: topic.id,
    }));
    const disabilityOptions = disabilities.map((disability) => ({
        key: disability.name,
        text: disability.name,
        value: disability.id,
    }));
    const initialState = {
        title: "",
        content: "",
        age_group: "",
        topics: [],
        disabilities: [],
    };

    // TODO: Get age groups from backend rather than hardcode
    const ageGroupOptions = [
        { key: "0-4", value: "0-4", text: "0-4" },
        { key: "4-11", value: "4-11", text: "4-11" },
        { key: "11-18", value: "11-18", text: "11-18" },
        { key: "18-25", value: "18-25", text: "18-25" },
        { key: "N/A", value: "N/A", text: "N/A" },
    ];
    const [state, setState] = useState(initialState);

    const dispatch = useDispatch();

    useEffect(() => {
        dispatch(getTopics());
        dispatch(getResources());
    }, [dispatch]);

    const onSubmit = (e) => {
        e.preventDefault();
        const post = {
            title: state.title,
            content: state.content,
            author: author.id,
            topics: state.topics,
            disabilities: state.disabilities,
        };
        console.log(post);
        dispatch(addPost(post));
        setState(initialState);
    };

    return (
        <Form onSubmit={onSubmit}>
            <Form.Input
                required
                label="Title"
                id="title"
                value={state.title}
                onChange={(e, { value }) =>
                    setState({ ...state, title: value })
                }
            />
            <Form.TextArea
                required
                label="Content"
                id="content"
                value={state.content}
                onChange={(e, { value }) =>
                    setState({ ...state, content: value })
                }
            />
            <Form.Dropdown
                fluid
                placeholder="Age Group"
                label="Age Group"
                options={ageGroupOptions}
                value={state.age_group}
                onChange={(e, { value }) =>
                    setState({ ...state, age_group: value })
                }
            />
            <Form.Dropdown
                fluid
                multiple
                selection
                placeholder="Topics"
                label="Topics"
                options={topicOptions}
                value={state.topic}
                onChange={(e, { value }) =>
                    setState({ ...state, topics: value })
                }
            />
            <Form.Dropdown
                fluid
                multiple
                selection
                placeholder="Disabilities"
                label="Disabilities"
                options={disabilityOptions}
                value={state.disabilities}
                onChange={(e, { value }) =>
                    setState({ ...state, disabilities: value })
                }
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
