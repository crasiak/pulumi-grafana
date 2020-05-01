# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class DataSource(pulumi.CustomResource):
    access_mode: pulumi.Output[str]
    basic_auth_enabled: pulumi.Output[bool]
    basic_auth_password: pulumi.Output[str]
    basic_auth_username: pulumi.Output[str]
    database_name: pulumi.Output[str]
    is_default: pulumi.Output[bool]
    json_datas: pulumi.Output[list]
    name: pulumi.Output[str]
    password: pulumi.Output[str]
    secure_json_datas: pulumi.Output[list]
    type: pulumi.Output[str]
    url: pulumi.Output[str]
    username: pulumi.Output[str]
    def __init__(__self__, resource_name, opts=None, access_mode=None, basic_auth_enabled=None, basic_auth_password=None, basic_auth_username=None, database_name=None, is_default=None, json_datas=None, name=None, password=None, secure_json_datas=None, type=None, url=None, username=None, __props__=None, __name__=None, __opts__=None):
        """
        Create a DataSource resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.

        The **json_datas** object supports the following:

          * `assumeRoleArn` (`pulumi.Input[str]`)
          * `authType` (`pulumi.Input[str]`)
          * `customMetricsNamespaces` (`pulumi.Input[str]`)
          * `defaultRegion` (`pulumi.Input[str]`)

        The **secure_json_datas** object supports the following:

          * `accessKey` (`pulumi.Input[str]`)
          * `secretKey` (`pulumi.Input[str]`)
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            __props__['access_mode'] = access_mode
            __props__['basic_auth_enabled'] = basic_auth_enabled
            __props__['basic_auth_password'] = basic_auth_password
            __props__['basic_auth_username'] = basic_auth_username
            __props__['database_name'] = database_name
            __props__['is_default'] = is_default
            __props__['json_datas'] = json_datas
            __props__['name'] = name
            __props__['password'] = password
            __props__['secure_json_datas'] = secure_json_datas
            if type is None:
                raise TypeError("Missing required property 'type'")
            __props__['type'] = type
            __props__['url'] = url
            __props__['username'] = username
        super(DataSource, __self__).__init__(
            'grafana:/dataSource:DataSource',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, access_mode=None, basic_auth_enabled=None, basic_auth_password=None, basic_auth_username=None, database_name=None, is_default=None, json_datas=None, name=None, password=None, secure_json_datas=None, type=None, url=None, username=None):
        """
        Get an existing DataSource resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.

        The **json_datas** object supports the following:

          * `assumeRoleArn` (`pulumi.Input[str]`)
          * `authType` (`pulumi.Input[str]`)
          * `customMetricsNamespaces` (`pulumi.Input[str]`)
          * `defaultRegion` (`pulumi.Input[str]`)

        The **secure_json_datas** object supports the following:

          * `accessKey` (`pulumi.Input[str]`)
          * `secretKey` (`pulumi.Input[str]`)
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["access_mode"] = access_mode
        __props__["basic_auth_enabled"] = basic_auth_enabled
        __props__["basic_auth_password"] = basic_auth_password
        __props__["basic_auth_username"] = basic_auth_username
        __props__["database_name"] = database_name
        __props__["is_default"] = is_default
        __props__["json_datas"] = json_datas
        __props__["name"] = name
        __props__["password"] = password
        __props__["secure_json_datas"] = secure_json_datas
        __props__["type"] = type
        __props__["url"] = url
        __props__["username"] = username
        return DataSource(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
