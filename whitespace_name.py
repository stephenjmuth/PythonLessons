first_name = " ada "
last_name = " lovelace "
full_name = f"{first_name} {last_name}"
#print(f"Hello, {full_name.title()}!")
print("Print name - no strip:")
print(f"\t{full_name}")
print("Print name - left strip:")
print(f"\t{full_name.lstrip()}")
print("Print name - right strip:")
print(f"\t{full_name.rstrip()}")
print("Print name - full strip:")
print(f"\t'{full_name.strip()}'")