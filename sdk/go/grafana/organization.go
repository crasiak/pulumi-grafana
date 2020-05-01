// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package grafana

import (
	"reflect"

	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

type Organization struct {
	pulumi.CustomResourceState

	AdminUser   pulumi.StringPtrOutput   `pulumi:"adminUser"`
	Admins      pulumi.StringArrayOutput `pulumi:"admins"`
	CreateUsers pulumi.BoolPtrOutput     `pulumi:"createUsers"`
	Editors     pulumi.StringArrayOutput `pulumi:"editors"`
	Name        pulumi.StringOutput      `pulumi:"name"`
	OrgId       pulumi.IntOutput         `pulumi:"orgId"`
	Viewers     pulumi.StringArrayOutput `pulumi:"viewers"`
}

// NewOrganization registers a new resource with the given unique name, arguments, and options.
func NewOrganization(ctx *pulumi.Context,
	name string, args *OrganizationArgs, opts ...pulumi.ResourceOption) (*Organization, error) {
	if args == nil {
		args = &OrganizationArgs{}
	}
	var resource Organization
	err := ctx.RegisterResource("grafana:/organization:Organization", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetOrganization gets an existing Organization resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetOrganization(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *OrganizationState, opts ...pulumi.ResourceOption) (*Organization, error) {
	var resource Organization
	err := ctx.ReadResource("grafana:/organization:Organization", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Organization resources.
type organizationState struct {
	AdminUser   *string  `pulumi:"adminUser"`
	Admins      []string `pulumi:"admins"`
	CreateUsers *bool    `pulumi:"createUsers"`
	Editors     []string `pulumi:"editors"`
	Name        *string  `pulumi:"name"`
	OrgId       *int     `pulumi:"orgId"`
	Viewers     []string `pulumi:"viewers"`
}

type OrganizationState struct {
	AdminUser   pulumi.StringPtrInput
	Admins      pulumi.StringArrayInput
	CreateUsers pulumi.BoolPtrInput
	Editors     pulumi.StringArrayInput
	Name        pulumi.StringPtrInput
	OrgId       pulumi.IntPtrInput
	Viewers     pulumi.StringArrayInput
}

func (OrganizationState) ElementType() reflect.Type {
	return reflect.TypeOf((*organizationState)(nil)).Elem()
}

type organizationArgs struct {
	AdminUser   *string  `pulumi:"adminUser"`
	Admins      []string `pulumi:"admins"`
	CreateUsers *bool    `pulumi:"createUsers"`
	Editors     []string `pulumi:"editors"`
	Name        *string  `pulumi:"name"`
	Viewers     []string `pulumi:"viewers"`
}

// The set of arguments for constructing a Organization resource.
type OrganizationArgs struct {
	AdminUser   pulumi.StringPtrInput
	Admins      pulumi.StringArrayInput
	CreateUsers pulumi.BoolPtrInput
	Editors     pulumi.StringArrayInput
	Name        pulumi.StringPtrInput
	Viewers     pulumi.StringArrayInput
}

func (OrganizationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*organizationArgs)(nil)).Elem()
}