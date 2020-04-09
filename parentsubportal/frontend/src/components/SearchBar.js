import _ from "lodash";
import React, { Component, useState, useEffect } from "react";
import { withRouter } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import { Search, Grid, Header, Segment } from "semantic-ui-react";
import { getResources } from "../actions/resources";

const initialState = { isLoading: false, results: [], value: "" };

function SearchBar(props) {
    const [{ isLoading, results, value }, setState] = useState(initialState);
    const dispatch = useDispatch();
    const sortedResources = useSelector(
        (state) => state.resources.resources
    ).reduce((acc, item) => {
        if (!acc[item.type]) {
            acc[item.type] = {};
            acc[item.type].name = item.type;
            acc[item.type].results = [];
        }
        var searchResult = {};
        const url = "/" + item.type + "s/" + item.data.id;
        var description = "topics: ";
        item.data.topic_names.forEach((item) => {
            description += item.name + " ";
        });

        searchResult.title = item.data.title;
        searchResult.url = url;
        searchResult.description = description;

        acc[item.type].results.push(searchResult);
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

    return (
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
    );
}

export default withRouter(SearchBar);
