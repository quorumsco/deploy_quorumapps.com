#!/bin/bash

fleetctl stop instances/*
fleetctl destroy instances/*
fleetctl start instances/*
