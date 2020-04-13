import React, { Component, Fragment, useState } from "react";
import { useDispatch, useSelector, useEffect } from "react-redux";
import {
    Dropdown,
    Button,
    Icon,
    Label,
    Item,
    Rating,
    Form,
    Modal,
    Select,
} from "semantic-ui-react";
import Comments from "./Comments";
import { ratePost, updateRating } from "../../../actions/ratings";
import { updateTimeline } from "../../../actions/timelines";

function PostDetail(props) {
    const [child, setChild] = useState(null);
    const user = useSelector((state) => state.auth.user);
    const timelines = useSelector((state) => state.timeline.timeline);
    const children = useSelector((state) => state.children.children);
    const childrenOptions = children.map((child) => ({
        key: child.id,
        text: child.first_name + " " + child.last_name,
        value: child.id,
    }));

    const dispatch = useDispatch();

    const inlineStyle = {
        modal: {
            marginTop: "0px !important",
            marginLeft: "50",
            marginRight: "50",
            height: "auto",
            top: "auto",
            left: "auto",
            bottom: "auto",
            right: "auto",
            overflow: "initial",
        },
    };

    // Returns the rating object for this post, or null if there isn't one
    const getRating = () => {
        // Filter all the ratings of this post based on logged in user's id
        const user_rating = props.post.ratings.filter(
            (rating) => rating.user === user.id
        );
        // If we found a rating, return its value else return a default of 0
        if (user_rating.length != 0) return user_rating[0];
        else return null;
    };

    // Returns the value of the rating, or 0 if this post is not rated by the user yet
    const getRatingValue = () => {
        const rating = getRating();
        if (rating == null) return 0;
        else return rating.rating;
    };

    // Updates the rating when clicked
    const checkRating = (e, data) => {
        const user_rating = getRating();
        var id = null;
        if (user_rating != null) id = user_rating.id;
        const rating = {
            id: id,
            rating: data.rating,
            user: user.id,
            content: props.post.id,
        };
        console.log(rating);
        dispatch(ratePost(rating));
        dispatch(updateRating(rating));
    };

    const handleAddToTimeline = () => {
        console.log(timelines);
        const t = timelines.filter((timeline) => timeline.child == child);
        console.log(t);
        if (t[0].content.includes(props.post.id)) {
            console.log("Already exists in timeline");
        } else t[0].content.push(props.post.id);
        dispatch(updateTimeline(t[0]));
    };

    const handleOnChange = (e, data) => {
        console.log(data.value);
    };

    const state = {
        options: [
            { key: "edit", icon: "edit", text: "Edit Post", value: "edit" },
            {
                key: "delete",
                icon: "delete",
                text: "Remove Post",
                value: "delete",
            },
        ],
    };

    return (
        <Fragment>
            <Item>
                <Item.Image
                    size="tiny"
                    src="https://react.semantic-ui.com/images/wireframe/image.png"
                />
                <Item.Content>
                    <Item.Header as="a">{props.post.title}</Item.Header>
                    <Item.Meta>
                        Posted by {props.post.author_username} on{" "}
                        {props.post.tidy_date}
                    </Item.Meta>
                    <Item.Description>{props.post.content}</Item.Description>
                    {props.children}
                    <Item.Extra>
                        Topics:{" "}
                        {props.post.topic_names.map((topic) => (
                            <Label href={"/topic/" + topic.name}>
                                {topic.name}
                            </Label>
                        ))}
                    </Item.Extra>
                    <Item.Extra>
                        Disabilities:{" "}
                        {props.post.disability_names.map((disability) => (
                            <Label href={"/disability/" + disability.name}>
                                {disability.name}
                            </Label>
                        ))}
                    </Item.Extra>
                    <Item.Extra>Age group: {props.post.age_group}</Item.Extra>
                    <Button.Group color="teal">
                        <Fragment>
                            <Modal
                                style={inlineStyle.modal}
                                trigger={<Button>Add To Timeline</Button>}
                            >
                                <Modal.Header>Add To Timeline</Modal.Header>
                                <Modal.Content>
                                    <Form onSubmit={handleAddToTimeline}>
                                        <Form.Group>
                                            <Form.Field
                                                required
                                                options={childrenOptions}
                                                label="Child"
                                                placeholder="Child"
                                                control={Select}
                                                value={child}
                                                onChange={(e, { value }) =>
                                                    setChild(value)
                                                }
                                            />
                                        </Form.Group>
                                        <Button
                                            content="Add"
                                            labelPosition="left"
                                            icon="edit"
                                            primary
                                        />
                                    </Form>
                                </Modal.Content>
                            </Modal>
                        </Fragment>
                        <Dropdown
                            className="button icon"
                            floating
                            options={state.options}
                            onChange={handleOnChange}
                            trigger={<React.Fragment />}
                        />
                    </Button.Group>
                    <Rating
                        maxRating={5}
                        defaultRating={getRatingValue()}
                        onRate={checkRating}
                        icon="star"
                        size="tiny"
                    />
                    Average rating: {props.post.avg_rating}
                </Item.Content>
            </Item>
            <Comments post={props.post} />
        </Fragment>
    );
}

export default PostDetail;
