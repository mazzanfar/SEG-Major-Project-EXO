import _ from "lodash";
import React, { Component, Fragment, useState, useEffect } from "react";
import { withRouter } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import {
    Search,
    Container,
    Dropdown,
    Grid,
    Header,
    Segment,
} from "semantic-ui-react";
import { getResources } from "../actions/resources";

const ageGroupOptions = [
    { key: "0-4", value: "0-4", text: "0-4" },
    { key: "4-11", value: "4-11", text: "4-11" },
    { key: "11-18", value: "11-18", text: "11-18" },
    { key: "18-25", value: "18-25", text: "18-25" },
    { key: "N/A", value: "N/A", text: "N/A" },
];

const initialState = {
    isLoading: false,
    results: [],
    value: "",
    ageGroups: [],
    contentTypes: [],
};

function SearchBar(props) {
    const [
        { isLoading, results, value, contentTypes, ageGroups },
        setState,
    ] = useState(initialState);
    const dispatch = useDispatch();
    const sortedResources = useSelector(
        (state) => state.resources.resources
    ).reduce((acc, item) => {
        // Check if the this result matches the selected content types and age groups
        if (
            ageGroups.indexOf(item.data.age_group) != -1 &&
            contentTypes.indexOf(item.type) != -1
        ) {
            if (!acc[item.type]) {
                acc[item.type] = {};
                acc[item.type].name = item.type;
                acc[item.type].results = [];
            }
            // Build the data to display as a rule
            var searchResult = {};
            const url = "/" + item.type + "s/" + item.data.id;
            var description = "topics:";
            item.data.topic_names.forEach((item) => {
                description += " " + item.name;
            });
            description += ", age group: " + item.data.age_group;

            searchResult.title = item.data.title;
            searchResult.url = url;
            searchResult.description = description;

            acc[item.type].results.push(searchResult);
        }
        return acc;
    }, {});

    useEffect(() => {
        dispatch(getResources());
    }, [dispatch]);

    const clearState = () => {
        setState({ ...initialState });
        return initialState;
    };

    const handleResultSelect = (e, { result }) => {
        props.history.push(result.url);
    };

    const handleSearchChange = (e, { value }) => {
        setState((prevState) => ({
            ...prevState,
            isLoading: true,
            value: value,
        }));
        setTimeout(() => {
            if (value.length < 1) return clearState();

            const re = new RegExp(_.escapeRegExp(value), "i");
            const isMatch = (result) => re.test(result.title);

            const filteredResults = _.reduce(
                sortedResources,
                (memo, data, name) => {
                    const results = _.filter(data.results, isMatch);
                    if (results.length) memo[name] = { name, results }; // eslint-disable-line no-param-reassign
                    return memo;
                },
                {}
            );

            setState((prevState) => ({
                ...prevState,
                isLoading: false,
                results: filteredResults,
            }));
        }, 300);
    };

    const contentTypeOptions = [
        {
            key: "pdf",
            text: "pdf",
            value: "pdf",
            image: {
                avatar: true,
                src:
                    "https://react.semantic-ui.com/images/avatar/small/jenny.jpg",
            },
        },
        {
            key: "video",
            text: "video",
            value: "video",
            image: {
                avatar: true,
                src:
                    "https://react.semantic-ui.com/images/avatar/small/elliot.jpg",
            },
        },
        {
            key: "post",
            text: "post",
            value: "post",
            image: {
                avatar: true,
                src:
                    "https://react.semantic-ui.com/images/avatar/small/stevie.jpg",
            },
        },
    ];

    return (
        <Fragment>
            <br />
            <Grid centered>
                <Search
                    category
                    loading={isLoading}
                    onResultSelect={handleResultSelect}
                    onSearchChange={_.debounce(handleSearchChange, 500, {
                        leading: true,
                    })}
                    results={results}
                    value={value}
                />
                <Dropdown
                    selection
                    multiple
                    placeholder="Content Types"
                    label="Content Types"
                    value={contentTypes}
                    options={contentTypeOptions}
                    onChange={(e, { value }) => {
                        setState((prevState) => ({
                            ...prevState,
                            contentTypes: value,
                        }));
                    }}
                />
                <Dropdown
                    selection
                    multiple
                    placeholder="Age Group"
                    label="Age Group"
                    value={ageGroups}
                    options={ageGroupOptions}
                    onChange={(e, { value }) => {
                        setState((prevState) => ({
                            ...prevState,
                            ageGroups: value,
                        }));
                    }}
                />
            </Grid>
        </Fragment>
    );
}

export default withRouter(SearchBar);
