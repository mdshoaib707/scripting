#!/usr/bin/env bash

exec java -Xms64m -Xmx64m -XX:MaxMetaspaceSize=67108864 -DdumpAwsContext=true -DconsulConfig=Digital_Manager -Dlog4j.configurationFile=/opt/camelSplitter/log4j2-camelSplitterDigital_Manager.xml -cp /opt/camelSplitter/is-splitter-1.0-SNAPSHOT-jar-with-dependencies.jar com.scholastic.integration.startup.AWSStartupStrategy
